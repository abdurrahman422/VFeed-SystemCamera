# Build and acceptance

## M0 local checks

From repository root in PowerShell:

```powershell
python -m py_compile tools/diagnostics/validate_bootstrap.py
python tools/diagnostics/validate_bootstrap.py
 git diff --check
```

There is no Android component to compile at M0. These checks validate the bootstrap artifact only. Record exact outcomes in COMMAND_LOG.md before committing.

## Platform prerequisite

Use a supported Linux AOSP build environment. Choose and pin a release manifest, record repo manifest revisions and toolchain, build and boot an unmodified Cuttlefish image first. Android 13 is the source inspection baseline, not a claim of universal later-release compatibility. Confirm target via the selected branch's Cuttlefish documentation; do not invent a lunch product or assume Windows can run Soong.

Place this repository under the selected checkout, for example vendor/vfeed, and add its product fragment after M1 has real modules. Resolve interface versions, VINTF compatibility, namespace visibility, provider names, camera identities and policy against that checkout. Record actual envsetup, lunch, m and launch commands with exit codes and artifacts. No executable platform command is prescribed until that product exists.

## M1 acceptance protocol

1. Compile the provider and Camera2 test app using Soong; fix every compilation error.
2. Boot Cuttlefish with enforcing SELinux and the additional provider. Confirm init and VINTF service registration.
3. Record adb shell dumpsys media.camera and service/provider logs; enumeration must include the additional camera without removing baseline cameras.
4. Test app uses CameraManager.getCameraIdList(), identifies the configured VFeed camera by its verified characteristics, opens it and requests repeating YUV_420_888 preview. A missing camera fails the test.
5. Run 640x480 and 1280x720 separately at 30 fps. Validate decoded color-bar pixels, continuous changing frame sequence, frame/result matching and strictly increasing timestamps for at least 60 seconds per size. Capture visual preview evidence and measured cadence/drop counts.
6. Close/reopen and test flush. Confirm no physical-camera dependency, CameraService crash, leaked buffers or SELinux denials.
7. Run applicable camera AIDL VTS from the selected checkout. Record exact suite/module names, logs and skipped cases with reasons; do not invent a passing VTS result.

M1 is complete only with actual Android build and runtime evidence. Stop before M2 if unavailable or failing.

## Later automated cases

M2 checks every advertised size/fps/stream combination and complete characteristics. M3 checks AVC sample fixtures, 24/25/30 fps, 720p/1080p, EOS loop, transforms and malformed/missing/unsupported media. M4 fault injection covers overflow, underrun, disconnect and decoder restart. M5 verifies SAF import/access enforcement and the full user flow. M6 automates repeated open/close, 30-minute playback, resolution changes, app/service/CameraService deaths, timestamp monotonicity, orientation, mirror and enforcing SELinux. Fixtures record hashes and expected pixel outputs; bad input must produce an observable error plus fallback.

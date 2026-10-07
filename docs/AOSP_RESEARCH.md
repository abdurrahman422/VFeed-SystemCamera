# Official AOSP source research

Inspected 2026-10-07 using Gitiles JSON directory listings and TEXT source responses from the official android.googlesource.com server. No upstream source was copied into this repository. The android13-release branch is an inspection baseline; record a complete pinned manifest before compiling M1.

| Required location | Inspected tree object | Official source |
| --- | --- | --- |
| Google AIDL service | 401309177bcb2ff4c12c67425e1e82e4f047be87 | https://android.googlesource.com/platform/hardware/google/camera/+/refs/heads/android13-release/common/hal/aidl_service/ |
| Provider AIDL | b94e05bb49c28db209d0174cc70599de81d1ed8f | https://android.googlesource.com/platform/hardware/interfaces/+/refs/heads/android13-release/camera/provider/aidl/ |
| Device AIDL | e670241e5ad5bdb97cb88963af8f22c744553b98 | https://android.googlesource.com/platform/hardware/interfaces/+/refs/heads/android13-release/camera/device/aidl/ |
| Metadata AIDL | e85c535d2a82595e034c14f9827af36d0bcb7ae9 | https://android.googlesource.com/platform/hardware/interfaces/+/refs/heads/android13-release/camera/metadata/aidl/ |
| Common AIDL | a951280602c2e4eefb87add87cbad96d8f5e41af | https://android.googlesource.com/platform/hardware/interfaces/+/refs/heads/android13-release/camera/common/aidl/ |

## Source observations and implementation consequences

The Google aidl_service.cc uses AServiceManager_addService for eager registration and registerLazyService for lazy registration. Its VINTF XML declares AIDL version 1 with internal/0. Its filenames still contain @2.7; do not infer the actual interface protocol from the filename. VFeed will use a distinct instance, its own init and manifest entries, and eager startup for the generated prototype.

ICameraProvider.aidl defines provider instance naming, device names, enumeration and getCameraDeviceInterface. Read the full naming and callback contracts against the pinned revision during M1, especially initial enumeration versus availability callbacks for external devices. A service registration alone does not establish a usable camera.

ICameraDeviceSession.aidl covers configureStreams, request processing, metadata queues, cache eviction, flush and close. Flush must finish all outstanding buffers/requests; close ends the session. Generated pixels alone do not satisfy these contracts. Use the target mapper/gralloc API and real fences rather than assuming contiguous YUV buffers.

Metadata Android.bp defines a stable camera metadata AIDL interface with frozen version 1 on the inspected branch. Use its generated types plus the platform camera metadata serialization utilities. Common Status.aidl defines service-specific errors; map unsupported operations and bad inputs to the specified contract.

The provider directory includes vts. Select actual suite names from the chosen checkout before recording VTS commands. Later Android releases can change interface versions and required metadata; upgrade through explicit build and runtime validation.

These are research observations and proposed design decisions, not evidence of a built or registered VFeed provider.

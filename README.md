# VFeed System Camera

A new Android 13+ platform project for a virtual camera fed by local video on the phone. The previous VFeed v1.1 project is a read-only reference and is not required or modified.

Pipeline: phone MP4 → VFeed Media Service → bounded frame transport → AIDL Camera Provider/HAL → CameraService → Camera1/Camera2 clients.

Current milestone: M0 bootstrap. No camera provider binary, MP4 decoder or Manager APK is implemented yet. See PROJECT_STATUS.md for verified results and environment blockers.

## Start here

- [Architecture](docs/ARCHITECTURE.md): process, control and data contracts.
- [AOSP research](docs/AOSP_RESEARCH.md): official interfaces and inspected sources.
- [Build and acceptance](docs/BUILD_AND_TEST.md): milestone gates and commands.
- [Roadmap](ROADMAP.md): required sequence and completion criteria.
- [Device profile](DEVICE_PROFILE.md): unknown physical-device facts.
- [Recovery policy](docs/RECOVERY.md): physical-device port prerequisites.

Run `python tools/diagnostics/validate_bootstrap.py` from the repository root. This verifies the documentation package, not Android runtime behavior. Platform components will use Android.bp as they are implemented and validated against the selected AOSP release. Empty build targets and fake HAL implementations are deliberately absent.

Normal operation must be entirely on the phone. AOSP build infrastructure is required only for development and installation. Prototype against Cuttlefish first; do not flash a physical phone in early milestones.

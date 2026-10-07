# Recovery and device-port gates

No physical-device flashing is authorized during M0–M6. Develop on AOSP/Cuttlefish first.

Never modify or erase bootloader, radio, modem, IMEI/EFS, persist, calibration or security-key partitions. Do not include commands targeting them in project tooling.

Before a later physical-device flash step, complete DEVICE_PROFILE.md, map only the necessary permitted partitions, document exact image provenance/checksums and matching factory recovery instructions, verify image availability and recovery entry, and record rollback steps with a tested recovery path. Include slot behavior, verified-boot requirements and data-loss consequences specific to that device. Unknown values block port work; generic fastboot instructions are insufficient.

This is a recovery policy, not a verified device-specific rollback procedure. No phone has been inspected or flashed.

# Roadmap

Each milestone requires a build, acceptance tests, compilation fixes, exact command records, a PROJECT_STATUS.md update and a commit before advancing. Runtime failures block advancement.

| Milestone | Scope | Acceptance gate |
| --- | --- | --- |
| M0 | Layout, architecture, research, gates | Bootstrap validator passes; contracts reviewed and committed |
| M1 | Single generated camera; no MP4 engine | Soong build passes; CameraManager enumerates VFeed; Camera2 opens and previews deterministic frames continuously at 640x480 and 1280x720, 30 fps without physical hardware |
| M2 | Characteristics and stream configuration | Complete characteristics dump; advertised combinations open and repeat stably; 24/25/30 fps validated; 1080p advertised only when supported |
| M3 | Separate MP4 engine | AVC MP4 720p/1080p at 24/25/30 fps; start/stop/pause/resume; loop/EOS restart; transforms and pacing verified independently |
| M4 | Shared queue integration | Bounded ownership, monotonic results, underrun fallback, decoder restart and consumer disconnect recovery verified |
| M5 | Manager APK | Import, preview, start/stop, loop, resolution, fps, rotation, mirror, fit/fill and live diagnostics work on target without a laptop |
| M6 | Automated reliability | Enumeration/open/close, repeated sessions, 30-minute playback, EOF, bad/missing media, unsupported codec, switching, deaths/restarts, queue faults, timestamps, transforms and SELinux tests; applicable AIDL camera VTS passes |
| Device port | Target-specific integration | Device profile complete; factory recovery verified; rollback documented; M0–M6 complete |

M1 initially supports one output preview stream and flexible YUV_420_888. Any additional output format, stream combination or advertised capability must be implemented and tested before exposure. Camera1 compatibility is a final integration objective and needs its own client test; it is not implied by Camera2 success. Audio replacement is outside the first version.

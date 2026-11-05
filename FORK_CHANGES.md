# MangaNest (placeholder name)

Independent Android fork of [Mangayomi](https://github.com/kodjodevf/mangayomi).
Upstream base: 5327b3c609971afb7785c01eb46a6afddc468c3c.

## Changes on 2026-11-05

- MangaNest launcher name, localized welcome text, in-app identity, and book icon.
- Teal Material 3 default palette; all existing theme choices remain available.
- Application ID: com.brandx50.manganest. Installs alongside the original.
- Default Android storage: /storage/emulated/0/MangaNest/.
- App updates and support links target brandx50-bit/mangayomi.
- Original license and attribution included in the app's license screen.
- An Android-only GitHub Actions workflow builds an installable debug APK.

## Build

The Android APK workflow runs on pushes to main and can be run manually.
Download the MangaNest-android-debug artifact from the completed run and unzip it.
This is a development APK signed with the runner's debug key. Each fresh runner
may use a different key; uninstall an older test build if Android rejects an
update (export a backup first). A stable private release signing key is needed
before production distribution. No app-store publishing is configured.

Internal Dart package names, native channel names, tracker callback schemes,
and backup formats retain upstream identifiers for compatibility. The name,
icon, package ID, and palette are provisional and can be replaced later.

See LICENSE and assets/manganest_NOTICE.txt for attribution and license terms.

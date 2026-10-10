# ESP Demo with Stream Mode

Standalone visual demo only; simulated targets do not connect to or interact with Free Fire.

## Controls
- **F8**: Toggle the demo ESP-style boxes, health bars, labels, distances, and guide lines.
- **F9**: Toggle Stream Mode, which hides all ESP-style demo elements for a clean scene.
- **Esc**: Quit.

## Build a Windows EXE using GitHub Actions (no local Python required)
1. Sign in at https://github.com/ and create a new repository.
2. Upload `esp_demo.py`, `requirements.txt`, and `.github/workflows/build.yml` while preserving the `.github/workflows` path.
3. Commit to the `main` branch.
4. Open **Actions** → **Build Windows EXE** → **Run workflow**.
5. After the run succeeds, open the run and download the `ESP_Demo-Windows` artifact.
6. Extract the ZIP to find `ESP_Demo.exe`.

Review the source and scan the downloaded executable with Microsoft Defender before running it.

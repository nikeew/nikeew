# Put this design on your GitHub profile

1. Create a **public** GitHub repository with a name exactly matching your GitHub username. If it already exists, use that repository.
2. Add `README.md`, the entire `assets` folder, `.github/workflows/snake.yml`, and `scripts/add_progress.py` at these exact paths. Upload the extracted files and folders, not the ZIP itself. Do not upload `SETUP.md` unless you want to keep these instructions in your profile repository.
3. In the repository, open **Actions → Update contribution snake → Run workflow**. The action generates the snake, combines it with the animated progress bar, and commits `assets/activity-dark.svg` and `assets/activity-light.svg` to the default branch. The combined animation appears in the README after that first successful run; the scheduled workflow refreshes it daily.
4. Visit your GitHub profile and check the banner, technology badges, and animated snake. Pin your real projects below the README through **Customize your pins**.

The right-hand image in the About section is `assets/moon-bolt.jpeg`. To show the other uploaded illustration instead, change that one path in `README.md` to `./assets/stardust.jpeg`.

The workflow needs permission to write repository contents. If GitHub blocks its push, check the repository's **Settings → Actions → General → Workflow permissions** and branch protection rules.

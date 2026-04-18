# Video-lectures

Structured **lecture** (`01_Lecture.md`) and **voice-over** (`02_VoiceOver.md`) content for Cambridge International **A-Level** and **O-Level** subjects, organised by syllabus code and topic.

## Layout

- `A-Level Subjects/` — topic folders per subject (e.g. Biology 9700, Mathematics 9709).
- `O-Level Subjects/` — same pattern for O Level codes.

## Git LFS (optional)

Large `.mp4` files are **ignored** by default so the repository stays suitable for GitHub without LFS. To track videos, install [Git LFS](https://git.lfs.github.com/), run `git lfs track "*.mp4"`, adjust `.gitignore`, then add and commit.

## Upload to GitHub

After creating an empty repository on GitHub:

```bash
cd /path/to/Video-lectures
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

Use SSH if you prefer: `git@github.com:YOUR_USERNAME/YOUR_REPO.git`.

## L08 — git-trainer

**What I built:** Practiced core Git workflows — branch, merge, rebase, cherry-pick, revert — in an isolated sandbox repo (`git-trainer`, kept separate from this monorepo to avoid nested-repo issues). Intentionally created and resolved both a merge conflict and a cherry-pick conflict.

**What I learned:**
- branch + merge: creating a branch, making divergent changes on the same line in two branches, and resolving the resulting conflict markers (<<<<<<< / ======= / >>>>>>>) by hand
- rebase vs merge: rebase rewrites history into a single linear sequence (no merge commit), while merge preserves both branches' history and adds an explicit merge commit
- cherry-pick: applying one specific commit from a branch without bringing in the rest of that branch's history — and that this can still conflict if the target branch is missing context lines the commit's diff depends on
- revert: creates a brand-new commit that undoes a previous commit's changes, rather than erasing it from history — safer for shared/pushed commits than rewriting history
- git log --oneline (and the graph view in VS Code) for visualizing how branch/merge/rebase/cherry-pick/revert actually shape commit history

**Where I got stuck:**
- git checkout main failed because the sandbox repo's default branch was still named master, not main
- the cherry-pick conflict could only be resolved by keeping a line from the "skipped" commit as context — learned that cherry-pick isn't always a perfectly isolated transplant
- revert removed more than expected (back to 3 lines instead of just undoing the last 2 added lines), because the diff being reverted was larger than anticipated due to how the conflict had been resolved earlier

**Time spent:** ~30 minutes
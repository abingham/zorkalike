We'll use this git repo to share code. We'll start simply and work up to more complex git interaction as we go.

If you're so inclined, you can learn all about git here: https://git-scm.com/doc

In the end this may be too much too fast, but I think it's worth a shot. 

# Getting a copy of this repository

First, you'll want to clone this repository to your pythonanywhere account. Open a bash console in pythonanywhere and run:
```
git clone https://github.com/abingham/zorkalike
```

This will print some stuff out, spin for a bit, and ultimately create a copy of this repository on your machine in a directory named "zorkalike".

# Getting updates

As I make changes to this repo, you'll want to pull them down using "git pull". Start another bash console, `cd` to the directory created in the clone operation, and run:
```
git pull
```

This will pull down any changes I've put into to the repository.

## Conflicting changes

A word of warning, though. If you've made any changes to the files in your copy when you do a pull, git may start trying to do merges and stuff. You may not want to deal with that yet.

To see if you've got any changes, run `git status`. If this doesn't say "working directory clean" at the end of its output, then you've got changes of some sort.

My advice is this. Prior to a pull, copy any changes you want to keep into some other other directory. Then do a `git reset --hard master` to reset your git repo to a clean state.

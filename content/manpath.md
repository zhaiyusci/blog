Title: MANPATH ${MANPATH} $(manpath)
Date: 2016-08-30 20:30
Category: Technology
Authors: Yu Zhai

In the past, I only set the shell variable `PATH` to make the software compiledby me can be found.

And after I installed TeXLive 2016 I learnt how to set `MANPATH`, which allows me to use man to browse the manual.

But today, I find what I was doing is absolutely wrong.

I use Linux Mint 18.

the way I set `MANPATH` was like this

```bash
export MANPATH=/path/to/the/man/page:${MANPATH}
```

Well, that is wrong because in this way, the `MANPATH` variable is set and the `mandb` no longer scans the system file `/etc/manpath.config`, which is relied by all the, how to say, native program.

If `mandb` runs, it will give a line like this

```
mandb: warning: $MANPATH set, ignoring /etc/manpath.config
```

The reason is that, in Ubuntu based system, as I read online, the MANPATH is null by default.  Yes, the system will create the database and yes, the `man` works for all the program like `ls` and all the program installed via `apt`.  But the system *does not* set the variable `MANPATH`.

The right way to set it is like this, as far as I tested

```bash
unset MANPATH
export MANPATH=$(manpath -q)
# somthing else
export MANPATH=/path/to/the/man/page:${MANPATH}
# something else
```

The second line up there is to set the MANPATH the initial value it should be as the `/etc/manpath.config` is sourced.  *Notice that the first line is also indispensible 'cause the `manpath` excutable will ignore `/etc/manpath.config` as well if `MANPATH` is set*.






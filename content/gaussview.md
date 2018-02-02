Title: How to use GaussView5 via ssh
Date: 2016-05-26 22:30
Category: Technology
Authors: Yu Zhai

Well, it seems that a lot of people (including the past me) do not know how to use GaussView in a server.  Say, it is fairly difficult to set the X server up.

[Prof. Li](http://huiligroup.org/) and I want to use it.  Actually, Prof. Li was going to let me help him install a copy on his Macbook.  However, we find that we do not have the copyright to do so.  But our institute do buy the software, at least for the server.  But we found it did not work.

The reason is that in the past IT engineer from ITC set the environment variable `DISPLAY` as a value (Why? I do not know).  And there do be some essay online told us that you should set things up in your `.bashrc` like this

```bash
export REMOTEHOST=`who am i | sed -n 's/.*(\([^) ]*\).*/\1/p; 1q'`
export DISPLAY=${REMOTEHOST}:0
```
Er, it is not that right.

Prof. Li told me that when he worked in uwaterloo, it is easy.  You can just type `ssh -Y xxx.xxx.xxx.xxx` to login and `gv`.  Well...

Back from Prof. Li's office, I find that what I am using, [MobaXterm](http://mobaxterm.mobatek.net/), can easily open its X server automatically.  It came to me that maybe there is something MobaXterm do but we do not know.  I check its setting and find it enable the X forwarding and I read the man page of ssh, it is what `-Y` do.  And what is more, MobaXterm can setup `DISPLAY` automatically.  So, maybe `ssh -Y` can do the same thing.  But there is some different.  I think `ssh -Y` will not change `DISPLAY` if it has been set, like this
```bash
if [ x$DISPLAY -ne x ]; then
    DISPLAY=xxx # I do not know what it actually does,
fi
```
So I comment out the line in `~/.bashrc` problem solved.

It is also true if you are using Molden from server.

And again, I recommend MobaXterm to you.

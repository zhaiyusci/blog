Title: How to set up remote ssh tunneling (port forward)
Date: 2019-04-21 22:30
Category: Technology
Authors: Yu Zhai

Computational resource of our institute is behind some firewall.

It means I need some method to connect to it if I am not in the office.
Even when I stay in the dormitory, I need some remote desktop software.

I used to use TeamViewer.  Recently I realized that TeamViewer treat the university as
some 'business environment'.  Sorry guys, I did not read the EULA carefully.
Besides, transfer the whole desktop via Internet is not a very good idea.
I have to say that TeamViewer does a good job.  I will use it for some special
case for personal affairs.  

Since I only need connect to ssh server actually, I learnt that port forwarding
is the right way.  I failed set it up in the past.  Now I believe I have find the
proper way to do that.  I take some notes here.

First thing first you need a VPS.  You need it any way if you are a Chinese scientist.
I got one from [Conoha.jp](https://www.conoha.jp/).  They accept Alipay as one of the payment method.
Moreover, they have a Chinese interface (but I really do not know way they do not have an English one,
perhaps they just focus on CJK market).

The VPS will have a public IP, which is important.  Then set the operating system. I use ubuntu.
If you are not sure, and only want set an ssh tunnely remote server, you can follow my 
choice. Follow what conoha tells you.  Set the root password, etc.

Make sure the ssh default port (22) is open in the panel.  After that, you should connect your VPS with
ssh.  

The key step is edit the file `/etc/ssh/sshd_config`.  Add the following lines:
```sshdconfig
# To solve break ssh tunneling problem 
# Ref: https://unix.stackexchange.com/questions/427189/how-to-cleanup-ssh-reverse-tunnel-socket-after-connection-closed
StreamLocalBindUnlink yes
```
By now, the remote part is finished.

Then the local part.  I have a Windows computer in my office.  So just open MobaXterm, click
'Tunneling' in the toolbar.  Set up a 'remote' tunneling rule. Like this

![Remote tunneling]({static}/img/mobatunnel.png)

Set the rule as auto start and reconnect if break.

Login your VPS then type:
```bash
ssh your_user_name@0.0.0.0 -p 10133
```

Enjoy!

---

Update 2019-05-01:

I found that MobaXterm is not good enough for this.  It losts connects often.
[Bitvise](https://www.bitvise.com/) is good.  Try it.


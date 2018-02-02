Title: Limit memory usage of a single process
Date: 2016-10-08 22:30
Category: Technology
Authors: Yu Zhai

If you are a computational scientist, I mean, not matter what you are working on, deep learning, computational physics, computational chemistry, etc., and if you use C++.  It is likely that you write a program to leak the momery.

It is a disaster!!!  Anyone run Linux on his/her own laptop and write a code like this
```cpp
int main()
{
    for(int i;i!=1;){
        new double;
    }
    return 0;
}
```

(I know the readers are not idiots and will not write program like this.) will find that your computer just dead in like a minute.  But frankly speaking, if you build a class and it has a construction function without a proper distruction function, and maybe one of the members of the class is a pointer, memory leaking happens, and this is a common mistake, even if you are a smart guy.

I also know that if you are a computational scientist you may not want to check if there is enough momery to "new" something, just because it is waste of time and come on, we are not professional programmer!

Therefore, when we debug a program in our laptop, what should we do?  A good choice is to put your program in a box.  If the memory inside the box runs out, just kill the program withour kill the mechine.

I am a Chinese.  So I search online in Chinese.  Unfortunately, there is not single one solution for this in Chinese world.  Luckily, there is one solution, which is exactly what we want. [Timeout](https://github.com/pshved/timeout) is a script that limit the memory and time use of a process.  To use it, it is simple
```bash
timeout -m 1000000 ./qmc.x -d 1000
```

Here, the '-m 1000000' is to set the maxium memory of the following command `./qmc.x -d 1000`, and the unit of the memory is KiB.

Well, it is not the manual of it. Just go the the github page for more information.

Finally, thanks to the author of the script, [Pavel Shved](http://coldattic.info/shvedsky/pro/blogs/a-foo-walks-into-a-bar).

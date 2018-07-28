Title: Install kdenlive on Windows
Date: 2018-07-29 02:10
Category: Tech
Authors: Yu Zhai

[kdenlive](https://kdenlive.org/en/) is a free software used to edit videos.  Although there is 'kde' in its name, it can be used on Windows.

The [official download page](https://kdenlive.org/en/download/) has provided a version for Windows.  However, it does not work at the first step: including your raw videos in the clip bin.  

This problem occurs because provided zip package does not place the ffmpeg library correctly.  Although on the download page it says, and I quote here 'Now, you don’t need to do anything more to set up. To run Kdenlive, you just have to unzip the downloaded Kdenlive version, and start Kdenlive from kdenlive.exe in kdenlive-windows folder.'

Here is the full steps to make it work:
* Download the `Kdenlive-xx.yy.zz-w64.zip` package [here](https://files.kde.org/kdenlive/release/Kdenlive-18.04.1d-w64.zip) (the lastest version should be download from the official page).
* Unzip `Kdenlive-xx.yy.zz-w64.zip` to `C:\kdenlive\`
* Download ffmpeg library [here](https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20180726-bce4da8-win64-static.zip)
* Open the ffmpeg zip package and drop 'n' drop to `C:\kdenlive\`.  After that you can see the `bin` directory appears in `C:\kdenlive\`.

Now double click the `kdenlive.exe` try to load a video in the bin.  All format supported by ffmpeg should now be supported by kdenlive.  

Enjoy!

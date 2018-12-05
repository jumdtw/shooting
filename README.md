# shooting  

##はじめに  
前提として、python3.x.x。  
無論pygameがないとできないので、インストール  
`python -m pip install pygame` 
あたりで可能。その後  
`python main.py`  
で遊べる。  

##windows  
windowsで実行使用とするとpygameのデフォルトのフォントが使えないためそのあたりを編集しなければならない。

##wiiリモコン  
参考記事  
http://yoshichi9.hatenablog.com/entry/2017/09/21/021651  
ubuntu のみで動作確認している。  
`sudo apt-get install automake`  
`sudo apt-get install autotool-dev`  
`sudo apt-get install autotools-dev`  
`sudo apt-get install bison`  
`sudo apt-get install flex`  
`sudo apt-get install libcwiid-dev`  
`sudo apt-get install bluetooth`  
`sudo apt-get install bluez-utils`  
`sudo aclocal`  
`sudo autoconf`  
`sudo ./configure`   
`sudo make install`  
でいける
環境汚れるので将来的にはコンテナを作りたい。
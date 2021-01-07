# Color & Monochrome
![モノクロ鏡餅](https://user-images.githubusercontent.com/51734722/103845942-79b91080-50e0-11eb-9f83-d6c5564e5aa1.jpg)

## リポジトリの概要
講義で作ったパッケージのカラーのみの映像のほかにモノクロの映像も映せるようにしたものです。

## デモ動画
YouTube:https://youtu.be/G-7kBRANYp0

## 動作環境
・OS : Ubuntu 20.04
・ROS noetic
・Python 3

## 使用機器
・Raspberry Pi 4 Model B
・webカメラ

## インストール方法
・ROS のインストール
　参考：[Ryuichi Ueda](https://github.com/ryuichiueda)氏の[ros_setup_scripts_Ubuntu20.04_server](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)

・cv_cameraとweb_video_serverのインストール
　参考：[Ryuichi Ueda](https://github.com/ryuichiueda)氏の[ロボットシステム学第10回(ROS)](https://ryuichiueda.github.io/robosys2020/lesson10_ros.html)

## 実装方法
インストール方法に従いROSを導入し、cv_cameraとweb_video_serverを利用できるようにしてください。

```
$ cd catkin_ws/src
$ git clone https://github.com/SotaSakakibara/RobotSystem2020_task2.git
```

## 実行方法
・端末1 
```
$ roscore &
$ rosrun cv_camera cv_camera_node
```
・端末2
```
$ rosrun web_video_server web_video_server
```
・端末3
```
$ rosrun mypkg monochrome.py
```

## 確認方法
・同じネットワーク内のPC,携帯などの端末のブラウザに
```
Raspberry Pi 4のIPアドレス:8080
```
　を入力します。

・すると、以下の画像の画面が表示されるので、image_rawを選択すればカラー映像、image_monochromeを選択すればモノクロ映像になります。
![モノクロ鏡餅解説](https://user-images.githubusercontent.com/51734722/103847406-7d9a6200-50e3-11eb-93e3-616ed76fda58.jpg)

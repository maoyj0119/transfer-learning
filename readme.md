# transfer learning 

@ author 姬小野

--- 迁移学习对五种花分类

## 环境
ubuntu 18.04

## requirements
1. torch==1.1.0
2. numpy==1.17.0
3. torchvision==0.3.0

## 使用方法
### 训练

下载vgg的预训练模型
`download.pytorch.org/models/vgg16-397923af.pth`放到目录`/home/jamey/.cache/torch/checkpoints`下
执行
`python train.py` 

即可在当前目录下训练自己的模型

ps. 在普通笔记本上生成模型的时间较久

### 测试

执行

`python test.py`

即可测试模型对花分类的准确率



当epoch为3时, 模型的准确率达到了83%, 其中, 除roses外准确率都极高. (大多数错误都是由roses引起的)

```bash
Test Accuracy of daisy: 84% (78/92)
Test Accuracy of dandelion: 94% (125/132)
Test Accuracy of roses: 59% (54/91)
Test Accuracy of sunflowers: 85% (86/101)
Test Accuracy of tulips: 87% (108/124)

Test Accuracy (Overall): 83% (451/540)
```



### 运行

对一张图片进行分类

```bash
----------------usage----------------
    run the demo with:
    python demo.py -m model_name -i image_name.jpg
    python demo.py --image image_name.jpg
    python demo.py -i image_name.jpg
    or use `python demo.py -h` to get help
    -----------------end-----------------
```

## 例子

### demo 1

![](./image/yvjingxiang_1.png)

```bash
$ python demo.py -m my_vgg16_3epochs.pth -i image/yvjingxiang_1.png
郁金香
```

demo.py 的输出结果是图片的识别的花的中文名

### demo 2

![](./image/pugongying_1.png)

```bash
$ python demo.py -m my_vgg16_3epochs.pth -i image/pugongying_1.png
蒲公英
```


# aosp-download-tool
从清华大学AOSP开源软件镜像站下载指定仓库代码的工具

## 使用方法
```
$ python code_fetcher.py -h
code_fetcher.py -d download_top_dir -m manifest.xml [-b branch]

$ python code_fetcher.py -d nfc -m manifests/nfc-manifest.xml

$ python code_fetcher.py -d nfc -m manifests/nfc-manifest.xml -b master
```
> 默认是下载android10-release分支，可以使用-b选项指定下载分支，其他分支名可以通过下载一个仓库后git branch -a查看

## 鸣谢
感谢[清华大学开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/AOSP/)的无私贡献。
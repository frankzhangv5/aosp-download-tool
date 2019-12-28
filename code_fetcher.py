#coding=utf-8
import xml.dom.minidom
import os
import sys,getopt

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "too few args, need 1 more at least"
        print "try '%s -h' for more information" % sys.argv[0]
        sys.exit()

    opts, args = getopt.getopt(sys.argv[1:], "hd:m:b:")
    
    top_dir = ''
    manifest_file = ''
    repo_branch = 'android10-release'
    
    for op, val in opts:
        if op == '-d':
            top_dir = val
        elif op == '-m':
            manifest_file = val
        elif op == '-b':
            repo_branch = val
        elif op == '-h':
            print "%s -d download_top_dir -m manifest.xml [-b branch]" % sys.argv[0]
            sys.exit()
        else:
            print "try '%s -h' for more information" % sys.argv[0]
            sys.exit()
    
    if top_dir is None:
        print "err: download top dir can't be null"
        sys.exit();
    
    if manifest_file is None:
        print "err: manifest file can't be null"
        sys.exit()
    
    repo_prefix = "https://aosp.tuna.tsinghua.edu.cn/"
    repo_suffix = ".git"

    top_dir = os.path.abspath(top_dir)
    if not os.path.exists(top_dir):
            os.makedirs(top_dir)
    print "Downloading code to", top_dir

    manifest_dom = xml.dom.minidom.parse(manifest_file)

    for node in manifest_dom.getElementsByTagName('project'):
        repo_dir = node.getAttribute('path')
        repo_name = node.getAttribute('name')
        os.chdir(top_dir)
        if not os.path.exists(repo_dir):
            os.makedirs(repo_dir)
        
        cmd = ' '.join(['git', 'clone', repo_prefix + repo_name + repo_suffix, '-b', repo_branch, repo_dir])
        print cmd
        os.system(cmd)
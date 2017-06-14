import filecmp

dir1 = 'E:/myprojects/solarwind/data/filtered/'
dir2 = 'E:/myprojects/solarwind/data/stage1/'

results = filecmp.dircmp(dir1, dir2)

print results.left_only
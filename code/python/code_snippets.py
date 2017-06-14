
        """
        dir1 = 'E:/myprojects/pv_detection/data/filtered/'
        dir2 = outPath
        
        results = filecmp.dircmp(dir1, dir2)
        
        flist = results.left_only
        newList = []
        for f in flist:
            f = dir1+f
            newList.append(f)
            
        print len(newList)
        """
        
        
     '''
        #profiling 2
        start = time.time()    
        for f in flist:
            print f
            faultDetection(f)
        
        end = time.time()
        runtime = end - start
        msg = "Single Thread Took {time} seconds to complete"
        print(msg.format(time=runtime))
    '''
        
    '''
        #dir1 = 'E:/myprojects/pv_detection/data/filtered/'
        #dir2 = 'E:/myprojects/pv_detection/data/stage1/'
        
        #results = filecmp.dircmp(dir1, dir2)
        
        #flist = results.left_only
        #newList = []
        #for f in flist:
        #    f = dir1+f
        #    newList.append(f)
    '''
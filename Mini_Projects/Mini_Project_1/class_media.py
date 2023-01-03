class Media():
    def __init__(self,n,d,i_s,u,dura,c):
       self.name = n
       self.duration  = d
       self.imdb_score = i_s
       self.url = u
       self.duration = dura
       self.casts = c
        
    def Show_menu(self):
        print("1-Add") 
        print("2-Edit")    
        print("3-Removoe")    
        print("4-Search")
        print("5-Show List")
        print("7-Exit") 
    
    # def download(self):
        # url=self.url
        # yt = YouTube(url)
        # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

class Actor():
    def __init__(self,casts):
        self.casts = casts




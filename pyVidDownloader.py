import yt_dlp #imports the yt_dlp library

def download_video(url):   #defines a function named download_video that takes one parameter url
    ydl_opts = {   #defines a dictionary named ydl_opts
        'format': 'best',  #downloads the best available quality
        'outtmpl': '%(title)s.%(ext)s',  #(output template) save the video with its title
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:  #with statement ensures that the resources are managed properly
        ydl.download([url])

if __name__ == "__main__":   #checks if the script is being executed as the main program
    video_url = input("Enter the video URL to be downloaded: ")   #asks the user for video link  
    download_video(video_url)

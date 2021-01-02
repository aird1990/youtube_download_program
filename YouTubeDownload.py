# 1.簡単なダウンロード方法
# 2行目にダウンロードしたいyoutubeのurlを入れる
# 3行目にダウンロードしたいフォルダ指定
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# youtube = pytube.YouTube(url).streams.first().download('C:/Users/AIR-D/Desktop')



# 2.フォーマットリストを表示させる方法
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# format_list = pytube.YouTube(url).streams.all()
# for format in format_list:
#     print(format)



# 3.選択したフォーマット(itag)をダウンロードする方法　
# itag(　)の中に選択したitagの数字を入れる
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# youtube = pytube.YouTube(url).streams.get_by_itag(22).download('C:/Users/AIR-D/Desktop')




# 4.オーディオとビデオを1つのファイルに含むレガシーストリーム（「プログレッシブダウンロード」
# のitagリストを表示させる方法。ただし、解像度が720p以下の場合のみです。
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# format_list = pytube.YouTube(url).streams.filter(progressive=True).all()
# for format in format_list:
#     print(format)



# 5.音声のみのitagを表示させる方法
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# format_list = pytube.YouTube(url).streams.filter(only_audio=True).all()
# for format in format_list:
#     print(format)



# 6.一番解像度の高いitag
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# format_list = pytube.YouTube(url).streams.filter(mime_type='video/mp4').order_by('resolution').desc().first()

# print(format_list)



# 7.解像度の高い順に全て並べる
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# format_list = pytube.YouTube(url).streams.filter(mime_type='video/mp4').order_by('resolution').desc().all()

# print(format_list)



# 8.レガシーストリーム(映像と音声を両方備えてるファイル)を解像度の高い順に全て並べる
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# format_list = pytube.YouTube(url).streams.filter(progressive=True).order_by('resolution').desc().all()

# print(format_list)




# 9.レガシーストリームの中で一番解像度の高いitag
# import pytube
# url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
# format_list = pytube.YouTube(url).streams.filter(progressive=True).order_by('resolution').desc().first()

# print(format_list)



# 10.レガシーストリームの中で一番解像度の高いitagをダウンロード
import pytube
url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'
format_list = pytube.YouTube(url).streams.filter(progressive=True).order_by('resolution').desc().first().download('C:/Users/AIR-D/Desktop')

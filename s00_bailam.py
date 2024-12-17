#region debai
"""
--- ma debai / id
greeting(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday
   https://github.com/namgivu/toyagreetinghourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo trinhduyetweb de kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamurl

02b dán diachi githubbailamurl theo mẫu ở trang web duoiday
    https://forms.gle/oXmPGxt3NTorcGnN8

--- debai / problem
Viết hàm
  greeting(hour_str)
giúp chat bot in ra câu chào theo buổi sáng/chiều/tối trong ngày
00:00AM  - 11:59AM Good morning!
12:00PM  - 05:59PM Good afternoon!
06:00PM  - 11:59PM Good evening!

Khi chạy với đầuvào / input  | Kếtquả đẩura / output  | Thứtự mẫuthử
---------------------------- | ---------------------- | -----------
greeting(hour_str='6am')     | Good morning!          | 00

# AM / PM format
greeting('6am')              | Good morning!          | 01
greeting('6 am')             | Good morning!          | 02
greeting('6AM')              | Good morning!          | 03
greeting('6 AM')             | Good morning!          | 04

greeting('9pm')              | Good evening!          | 05
greeting('0900pm')           | Good evening!          | 06
greeting('09:00pm')          | Good evening!          | 07
greeting('09:00 pm')         | Good evening!          | 08
greeting('09:00 PM')         | Good evening!          | 09

greeting('1pm')              | Good afternoon!        | 10

# 24-hours format
greeting('06:00')            | Good morning!          | 11
greeting('0600')             | Good morning!          | 12
greeting('21:00')            | Good evening!          | 13
greeting('2100')             | Good evening!          | 14

"""
#endregion debai

#region bailam

# def greetingTODO(hour_str): convert to 24h-format -> do greet

def greeting_regex(hour_str):  #NOT WORKING  ref https://g.co/bard/share/b2a94837d088
  import re
  m = re.findall(r"^(0[0-9]|1[0-1|2])[:]?([0-5][0-9])?\s*(?:[AaPp][Mm])$", hour_str)
  return m

def greeting(hour_str):
  pass#TODO
#endregion bailam
import string
import datetime


def image_naming_according_to_index(idx = 1, fn_len = 4, fn_ext = '.jpg'):
    fn = (str(idx)).zfill(fn_len-len(str(idx))+1)
    fn += fn_ext
    return fn


def image_naming_according_to_time(idx = 1, fn_ext = '.jpg'):
    fn = ''
    now = datetime.datetime.now()
    fn += str(now.year)
    fn += '-'
    fn += str(now.month)
    fn += '-'
    fn += str(now.day)
    fn += '-'
    fn += str(now.hour)
    fn += '-'
    fn += str(now.minute)
    fn += '-'
    fn += str(now.second)
    fn += '_'
    fn += (str(idx)).zfill(3-len(str(idx))+1)
    fn += fn_ext
    return fn



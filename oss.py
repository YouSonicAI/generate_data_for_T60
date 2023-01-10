import oss2
access_key_id = 'LTAI5tAzLJwWiQBHqX6ywLxa'
access_key_secret = 'R60PTPKqrMgPwli9dZjwL1Mp3xmCxR'
bucket_name = 'sti-user-file'
endpoint = 'https://oss-cn-hangzhou.aliyuncs.com'

auth = oss2.Auth(access_key_id, access_key_secret)

bucket = oss2.Bucket(auth, endpoint, bucket_name, connect_timeout=40)

file = '/root/Project/zip_floder/111_audio.zip'
file_name = file.split('/')[-1]
result = bucket.put_object_from_file(file_name, file)
# result = bucket.put_object(file, fileContent)
print('finished!!!!')
import base64, codecs
magic = 'IyBtYWRlIGJ5IFNuZWUjMTMzNyBhbmQgU2VucyM5NDQ4IG9uIGRpc2NvcmQsIHdhbnQgbW9yZSBwcm9ncmFtbXM/IHRha2UgYSBsb29rIGF0IGh0dHBzOi8vYml0Lmx5L3NlbnNhbHRzDQojIHNraWRkaW5nIGRvZXNuJ3QgbWFrZSB5b3UgY29vbCBvciBhIGNvZGVyIDspDQoNCmZyb20gcmVxdWVzdHMgaW1wb3J0IGdldCwgcG9zdA0KZnJvbSByYW5kb20gaW1wb3J0IHJhbmRpbnQNCg0KY2xhc3MgYmNvbG9yczoNCiAgICBIRUFERVIgPSAnXDAzM1s5NW0nDQogICAgT0tCTFVFID0gJ1wwMzNbOTRtJw0KICAgIE9LQ1lBTiA9ICdcMDMzWzk2bScNCiAgICBPS0dSRUVOID0gJ1wwMzNbOTJtJw0KICAgIFdBUk5JTkcgPSAnXDAzM1s5M20nDQogICAgRkFJTCA9ICdcMDMzWzkxbScNCiAgICBFTkRDID0gJ1wwMzNbMG0nDQogICAgQk9MRCA9ICdcMDMzWzFtJw0KICAgIFVOREVSTElORSA9ICdcMDMzWzRtJw0KDQoNCnByaW50KGJjb2xvcnMuT0tHUkVFTiArIGJjb2xvcnMuQk9MRCArICJtYWRlIGJ5IFNuZWUjMTMzNyBhbmQgU2VucyM5NDQ4IG9uIGRpc2NvcmQsIHdhbnQgbW9yZSBwcm9ncmFtbXM/IHRha2UgYSBsb29rIGF0IGh0dHBzOi8vYml0Lmx5L3NlbnNhbHRzIiArIGJjb2xvcnMuRU5EQykNCg0KZ'
love = 'TIzVUMupzyuoaDkXUEin2IhXGbAPvNtVPOlMKAjo25mMFN9VTqyqPtanUE0pUZ6Yl9xnKAwo3WxYzAioF9upTxiqwLiLKI0nP9fo2qcovpfVTuyLJEypaZ9rlWOqKEbo3WcrzS0nJ9hVwbtqT9eMJ59XFAPLJDtqzSlnJShqPOzo3VtoJSmplO0o2gyovOwnTIwnlOxqJHtqT8tqTuyVUWuqTHtoTygnKDhQDbtVPNtpzI0qKWhVSElqJHtnJLtpzImpT9hp2Hhp3EuqUImK2AiMTHtCG0tZwNjVTIfp2HtEzSfp2HAPt0XMTIzVUMupzyuoaDlXUEin2IhXGbAPvNtVPOlMKAjo25mMFN9VUOip3DbMvqbqUEjpmbiY2Ecp2AipzDhL29gY2SjnF92Av9coaMcqTHir3WuozEcoaDbZFj5BGx5BGx5XK0aYPObMJSxMKWmCKfaDKI0nT9lnKcuqTyiovp6VUEin2IhsFxAPvNtVPOcMvNvJJ91VT5yMJDtqT8tqzIlnJM5VUyiqKVtLJAwo3IhqPOcovOipzEypvO0olOjMKWzo3WgVUEbnKZtLJA0nJ9hYvVtnJ4tp3ElXUWyp3OioaAyYzAioaEyoaDcVT9lVPV0ZQR6VSIhLKI0nT9lnKcyMPVtnJ4tp3ElXUWyp3OioaAyYzAioaEyoaDcBt0XVPNtVPNtVPOlMKE1pz4tEzSfp2HAPvNtVPOyoUAyBt0XVPNtVPNtVPOlMKE1pz4tIUW1MD0XQDcxMJLtqzSlnJShqQWsH3EuqUImXUEin2IhXGbAPvNtVPOlMKAjo25mMFN9VUOip3DbMv'
god = 'dodHRwczovL2Rpc2NvcmQuY29tL2FwaS92Ni9pbnZpdGUve3JhbmRpbnQoMSw5OTk5OTk5KX0nLCBoZWFkZXJzPXsnQXV0aG9yaXphdGlvbic6IHRva2VufSkNCiAgICBpZiByZXNwb25zZS5zdGF0dXNfY29kZSA9PSA0MDE6DQogICAgICAgIHJldHVybiAnSW52YWxpZCcNCiAgICBlbGlmICJZb3UgbmVlZCB0byB2ZXJpZnkgeW91ciBhY2NvdW50IGluIG9yZGVyIHRvIHBlcmZvcm0gdGhpcyBhY3Rpb24uIiBpbiBzdHIocmVzcG9uc2UuY29udGVudCk6DQogICAgICAgIHJldHVybiAnUGhvbmUgTG9jaycNCiAgICBlbHNlOg0KICAgICAgICByZXR1cm4gJ1ZhbGlkJw0KDQppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOg0KICAgIHRyeToNCiAgICAgICAgY2hlY2tlZCA9IFtdDQogICAgICAgIHdpdGggb3BlbigndG9rZW5zLnR4dCcsICdyJykgYXMgdG9rZW5zOg0KICAgICAgICAgICAgZm9yIHRva2VuIGluIHRva2Vucy5yZWFkKCkuc3BsaXQoJ1xuJyk6DQogICAgICAgICAgICAgICAgaWYgbGVuKHRva2VuKSA+IDE1IGFuZCB0b2tlbiBub3QgaW4gY2hlY2tlZCBhbmQgdmFyaWFudDIodG9rZW4pID09IFRydWU6DQogICAgICAgICAgICAgICAgICAgIHByaW50KGYnVG9rZW46IHt0b2tlbn0gaXMgVmF'
destiny = 'fnJDaXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPOwnTIwn2IxYzSjpTIhMPu0o2gyovxAPvNtVPNtVPNtVPNtVPNtVPOyoUAyBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPOjpzyhqPuzW1Ein2IhBvO7qT9eMJ59VTymVRyhqzSfnJDaXD0XVPNtVPNtVPOcMvOfMJ4bL2uyL2gyMPxtCvNjBt0XVPNtVPNtVPNtVPNtp2S2MFN9VTyhpUI0XTLar2kyovuwnTIwn2IxXK0tqzSfnJDtqT9eMJ5mKT5GLKMyVUEbMFO2LJkcMPO0o2gyoaZtqT8tEzyfMFNbrF9hXFpcYzkiq2IlXPxAPvNtVPNtVPNtVPNtVTyzVUAuqzHtCG0tW3xaBt0XVPNtVPNtVPNtVPNtVPNtVT5uoJHtCFOlLJ5xnJ50XQRjZQNjZQNjZPjtBGx5BGx5BGx5BFxAPvNtVPNtVPNtVPNtVPNtVPO3nKEbVT9jMJ4bMvq7ozSgMK0hqUu0WljtW3paXFOuplOmLKMyEzyfMGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtp2S2MHMcoTHhq3WcqTHbW1khWl5do2yhXTAbMJAeMJDcXD0XVPNtVPNtVPNtVPNtVPNtVUOlnJ50XTLaIT9eMJ5mVSAuqzHtIT8tr25uoJI9YaE4qPOTnJkyVFpcQDbtVPNtVPNtVTyhpUI0XPqDpzImplOSoaEypvOTo3VtEKucqP4hYvpcQDbtVPNtMKuwMKO0Bt0XVPNtVPNtVPOcoaO1qPtaD2ShLUDtG3OyovNvqT9eMJ5mYaE4qPVtEzyfMFRaXD0X'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

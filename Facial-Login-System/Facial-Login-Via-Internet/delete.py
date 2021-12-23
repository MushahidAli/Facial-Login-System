from imagekitio import ImageKit

imagekit = ImageKit(
    private_key='private_=U/oOY9GSaaaTff4k2W4o5t53fUq',
    public_key='public_=0CO8Za9flCPeGRxutlgQvLYvkea',
    url_endpoint='https://ik.imagekit.io/zhfxaap2nx3'
)

number = imagekit.list_files({
})

value = str(input("Please Enter Your UsernameID To Delete Your Account : "))
answer = value + ".jpg"

for i in number['response']:
    if i['name'] == answer:
      imagekit.delete_file(i['fileId'])

print("Your Account [ID="+value+"] Has Been Successfully Deleted!\nYour Account Still Will Exist For Some Time Before Being Fully Deleted!")
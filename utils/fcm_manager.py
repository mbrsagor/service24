# FCM
from fcm.utils import get_device_model, FCMMessage


Device = get_device_model()


# FCM Implementation
my_phone = Device.objects.get(name='mbr-sagor')
my_phone.send_message({'message': 'my test message'}, delay_while_idle=True, time_to_live=2)
# FCMMessage().send({'message': 'my test message'}, to='/topics/my-topic')

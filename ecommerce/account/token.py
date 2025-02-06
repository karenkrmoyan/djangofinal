
# - Import password reset token generator

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


# - Password reset token generator method

# - Below i am overriding the _make_hash_value method to include additional data
#   (user's active status) alongside the standard user ID and timestamp

class UserVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = six.text_type(user.pk)
        ts = six.text_type(timestamp)
        is_active = six.text_type(user.is_active)
        return f"{user_id}{ts}{is_active}"

# - Creating an object to be used to generate tokens for users utilizing the overridden method

user_tokenizer_generate = UserVerificationTokenGenerator()
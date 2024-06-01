from rest_framework.serializers import Serializer, ModelSerializer

from transactions.models import Category, Transaction

# todo: seprate create and read serializers


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'avatar']
        read_only_fields = ['name', 'avatar']

    def create(self, validated_data):
        # TODO:handle perform crate in view
        return super().create(validated_data)


class TransactionSerializer(ModelSerializer):
    # TODO:handle bank account and category joins
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'transaction_type', 'amount', 'date', 'description', ]
        read_only_fields = ['transaction_id', 'date']

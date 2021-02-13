


class CancelSubscriptionResponse(BaseResponse):
	response = None


class ChangeStateResponse(BaseResponse):
	response = None


class GetAmountResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetUserSubscriptionByIdResponse(BaseResponse):
	response = None


class GetUserSubscriptionsResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class UpdateSubscriptionResponse(BaseResponse):
	response = None


CancelSubscriptionResponseModel = None


ChangeStateResponseModel = string


GetAmountResponseModel = None


GetByIdResponseModel = array


GetUserSubscriptionByIdResponseModel = None


class GetUserSubscriptionsResponse(BaseResponse):
	count = None
	items = None


GetResponseModel = array


UpdateSubscriptionResponseModel = None
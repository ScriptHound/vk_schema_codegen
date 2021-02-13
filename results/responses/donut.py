


class GetSubscriptionResponse(BaseResponse):
	response = None


class GetSubscriptionsResponse(BaseResponse):
	response = None


GetSubscriptionResponseModel = None


class GetSubscriptionsResponse(BaseResponse):
	subscriptions = None
	count = None
	profiles = None
	groups = None
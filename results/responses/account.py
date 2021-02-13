


class ChangePasswordResponse(BaseResponse):
	response = None


class GetActiveOffersResponse(BaseResponse):
	response = None


class GetAppPermissionsResponse(BaseResponse):
	response = None


class GetBannedResponse(BaseResponse):
	response = None


class GetCountersResponse(BaseResponse):
	response = None


class GetInfoResponse(BaseResponse):
	response = None


class GetProfileInfoResponse(BaseResponse):
	response = None


class GetPushSettingsResponse(BaseResponse):
	response = None


class SaveProfileInfoResponse(BaseResponse):
	response = None


class ChangePasswordResponse(BaseResponse):
	token = None
	secret = None


class GetActiveOffersResponse(BaseResponse):
	count = None
	items = None


GetAppPermissionsResponseModel = None


class GetBannedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


GetCountersResponseModel = None


GetInfoResponseModel = None


GetProfileInfoResponseModel = None


GetPushSettingsResponseModel = None


class SaveProfileInfoResponse(BaseResponse):
	changed = None
	name_request = None
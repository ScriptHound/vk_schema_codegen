

class ChangePasswordResponse(BaseResponse):
	token = None
	secret = None

class GetActiveOffersResponse(BaseResponse):
	count = None
	items = None

class GetAppPermissionsResponse(BaseResponse):
	

class GetBannedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None

class GetCountersResponse(BaseResponse):
	

class GetInfoResponse(BaseResponse):
	

class GetProfileInfoResponse(BaseResponse):
	

class GetPushSettingsResponse(BaseResponse):
	

class SaveProfileInfoResponse(BaseResponse):
	changed = None
	name_request = None
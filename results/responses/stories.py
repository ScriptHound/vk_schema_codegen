

class GetBannedExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None

class GetBannedResponse(BaseResponse):
	count = None
	items = None

class GetByIdExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None

class GetByIdResponse(BaseResponse):
	count = None
	items = None

class GetPhotoUploadServerResponse(BaseResponse):
	upload_url = None
	user_ids = None

class GetStatsResponse(BaseResponse):
	

class GetVideoUploadServerResponse(BaseResponse):
	upload_url = None
	user_ids = None

class GetViewersExtendedV5115Response(BaseResponse):
	count = None
	items = None
	hidden_reason = None

class GetViewersExtendedResponse(BaseResponse):
	count = None
	items = None

class GetV5113Response(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None
	need_upload_screen = None

class GetResponse(BaseResponse):
	count = None
	items = None
	promo_data = None
	profiles = None
	groups = None
	need_upload_screen = None

class SaveResponse(BaseResponse):
	count = None
	items = None

class UploadResponse(BaseResponse):
	upload_result = None
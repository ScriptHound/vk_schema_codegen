


class GetBannedExtendedResponse(BaseResponse):
	response = None


class GetBannedResponse(BaseResponse):
	response = None


class GetByIdExtendedResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetPhotoUploadServerResponse(BaseResponse):
	response = None


class GetStatsResponse(BaseResponse):
	response = None


class GetVideoUploadServerResponse(BaseResponse):
	response = None


class GetViewersExtendedV5115Response(BaseResponse):
	response = None


class GetViewersExtendedResponse(BaseResponse):
	response = None


class GetV5113Response(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class SaveResponse(BaseResponse):
	response = None


class UploadResponse(BaseResponse):
	response = None


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


GetStatsResponseModel = None


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
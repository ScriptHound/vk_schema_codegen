


class AddAlbumResponse(BaseResponse):
	response = None


class CreateCommentResponse(BaseResponse):
	response = None


class GetAlbumByIdResponse(BaseResponse):
	response = None


class GetAlbumsByVideoExtendedResponse(BaseResponse):
	response = None


class GetAlbumsByVideoResponse(BaseResponse):
	response = None


class GetAlbumsExtendedResponse(BaseResponse):
	response = None


class GetAlbumsResponse(BaseResponse):
	response = None


class GetCommentsExtendedResponse(BaseResponse):
	response = None


class GetCommentsResponse(BaseResponse):
	response = None


class GetExtendedResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class RestoreCommentResponse(BaseResponse):
	response = None


class SaveResponse(BaseResponse):
	response = None


class SearchExtendedResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


class UploadResponse(BaseResponse):
	response = None


class AddAlbumResponse(BaseResponse):
	album_id = None


CreateCommentResponseModel = None


GetAlbumByIdResponseModel = None


class GetAlbumsByVideoExtendedResponse(BaseResponse):
	count = None
	items = None


GetAlbumsByVideoResponseModel = array


class GetAlbumsExtendedResponse(BaseResponse):
	count = None
	items = None


class GetAlbumsResponse(BaseResponse):
	count = None
	items = None


class GetCommentsExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class GetCommentsResponse(BaseResponse):
	count = None
	items = None


class GetExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class GetResponse(BaseResponse):
	count = None
	items = None


RestoreCommentResponseModel = None


SaveResponseModel = None


class SearchExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class SearchResponse(BaseResponse):
	count = None
	items = None


class UploadResponse(BaseResponse):
	size = None
	video_id = None
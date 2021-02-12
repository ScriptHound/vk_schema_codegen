

class AddAlbumResponse(BaseResponse):
	album_id = None

class CreateCommentResponse(BaseResponse):
	

class GetAlbumByIdResponse(BaseResponse):
	

class GetAlbumsByVideoExtendedResponse(BaseResponse):
	count = None
	items = None

class GetAlbumsByVideoResponse(BaseResponse):
	

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

class RestoreCommentResponse(BaseResponse):
	

class SaveResponse(BaseResponse):
	

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
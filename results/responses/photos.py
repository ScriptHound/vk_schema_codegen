

class CopyResponse(BaseResponse):
	

class CreateAlbumResponse(BaseResponse):
	

class CreateCommentResponse(BaseResponse):
	

class DeleteCommentResponse(BaseResponse):
	

class GetAlbumsCountResponse(BaseResponse):
	

class GetAlbumsResponse(BaseResponse):
	count = None
	items = None

class GetAllCommentsResponse(BaseResponse):
	count = None
	items = None

class GetAllExtendedResponse(BaseResponse):
	count = None
	items = None
	more = None

class GetAllResponse(BaseResponse):
	count = None
	items = None
	more = None

class GetByIdExtendedResponse(BaseResponse):
	

class GetByIdResponse(BaseResponse):
	

class GetCommentsExtendedResponse(BaseResponse):
	count = None
	real_offset = None
	items = None
	profiles = None
	groups = None

class GetCommentsResponse(BaseResponse):
	count = None
	real_offset = None
	items = None

class GetMarketUploadServerResponse(BaseResponse):
	

class GetMessagesUploadServerResponse(BaseResponse):
	

class GetNewTagsResponse(BaseResponse):
	count = None
	items = None

class GetTagsResponse(BaseResponse):
	

class GetUploadServerResponse(BaseResponse):
	

class GetUserPhotosExtendedResponse(BaseResponse):
	count = None
	items = None

class GetUserPhotosResponse(BaseResponse):
	count = None
	items = None

class GetWallUploadServerResponse(BaseResponse):
	

class GetExtendedResponse(BaseResponse):
	count = None
	items = None

class GetResponse(BaseResponse):
	count = None
	items = None

class MarketAlbumUploadResponse(BaseResponse):
	gid = None
	hash = None
	photo = None
	server = None

class MarketUploadResponse(BaseResponse):
	crop_data = None
	crop_hash = None
	group_id = None
	hash = None
	photo = None
	server = None

class MessageUploadResponse(BaseResponse):
	hash = None
	photo = None
	server = None

class OwnerCoverUploadResponse(BaseResponse):
	hash = None
	photo = None

class OwnerUploadResponse(BaseResponse):
	hash = None
	photo = None
	server = None

class PhotoUploadResponse(BaseResponse):
	aid = None
	hash = None
	photo = None
	photos_list = None
	server = None

class PutTagResponse(BaseResponse):
	

class RestoreCommentResponse(BaseResponse):
	

class SaveMarketAlbumPhotoResponse(BaseResponse):
	

class SaveMarketPhotoResponse(BaseResponse):
	

class SaveMessagesPhotoResponse(BaseResponse):
	

class SaveOwnerCoverPhotoResponse(BaseResponse):
	

class SaveOwnerPhotoResponse(BaseResponse):
	photo_hash = None
	photo_src = None
	photo_src_big = None
	photo_src_small = None
	saved = None
	post_id = None

class SaveWallPhotoResponse(BaseResponse):
	

class SaveResponse(BaseResponse):
	

class SearchResponse(BaseResponse):
	count = None
	items = None

class WallUploadResponse(BaseResponse):
	hash = None
	photo = None
	server = None



class CopyResponse(BaseResponse):
	response = None


class CreateAlbumResponse(BaseResponse):
	response = None


class CreateCommentResponse(BaseResponse):
	response = None


class DeleteCommentResponse(BaseResponse):
	response = None


class GetAlbumsCountResponse(BaseResponse):
	response = None


class GetAlbumsResponse(BaseResponse):
	response = None


class GetAllCommentsResponse(BaseResponse):
	response = None


class GetAllExtendedResponse(BaseResponse):
	response = None


class GetAllResponse(BaseResponse):
	response = None


class GetByIdExtendedResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetCommentsExtendedResponse(BaseResponse):
	response = None


class GetCommentsResponse(BaseResponse):
	response = None


class GetMarketUploadServerResponse(BaseResponse):
	response = None


class GetMessagesUploadServerResponse(BaseResponse):
	response = None


class GetNewTagsResponse(BaseResponse):
	response = None


class GetTagsResponse(BaseResponse):
	response = None


class GetUploadServerResponse(BaseResponse):
	response = None


class GetUserPhotosExtendedResponse(BaseResponse):
	response = None


class GetUserPhotosResponse(BaseResponse):
	response = None


class GetWallUploadServerResponse(BaseResponse):
	response = None


class GetExtendedResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class MarketAlbumUploadResponse(BaseResponse):
	response = None


class MarketUploadResponse(BaseResponse):
	response = None


class MessageUploadResponse(BaseResponse):
	response = None


class OwnerCoverUploadResponse(BaseResponse):
	response = None


class OwnerUploadResponse(BaseResponse):
	response = None


class PhotoUploadResponse(BaseResponse):
	response = None


class PutTagResponse(BaseResponse):
	response = None


class RestoreCommentResponse(BaseResponse):
	response = None


class SaveMarketAlbumPhotoResponse(BaseResponse):
	response = None


class SaveMarketPhotoResponse(BaseResponse):
	response = None


class SaveMessagesPhotoResponse(BaseResponse):
	response = None


class SaveOwnerCoverPhotoResponse(BaseResponse):
	response = None


class SaveOwnerPhotoResponse(BaseResponse):
	response = None


class SaveWallPhotoResponse(BaseResponse):
	response = None


class SaveResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


class WallUploadResponse(BaseResponse):
	response = None


CopyResponseModel = None


CreateAlbumResponseModel = None


CreateCommentResponseModel = None


DeleteCommentResponseModel = None


GetAlbumsCountResponseModel = None


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


GetByIdExtendedResponseModel = array


GetByIdResponseModel = array


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


GetMarketUploadServerResponseModel = None


GetMessagesUploadServerResponseModel = None


class GetNewTagsResponse(BaseResponse):
	count = None
	items = None


GetTagsResponseModel = array


GetUploadServerResponseModel = None


class GetUserPhotosExtendedResponse(BaseResponse):
	count = None
	items = None


class GetUserPhotosResponse(BaseResponse):
	count = None
	items = None


GetWallUploadServerResponseModel = None


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


PutTagResponseModel = None


RestoreCommentResponseModel = None


SaveMarketAlbumPhotoResponseModel = array


SaveMarketPhotoResponseModel = array


SaveMessagesPhotoResponseModel = array


SaveOwnerCoverPhotoResponseModel = array


class SaveOwnerPhotoResponse(BaseResponse):
	photo_hash = None
	photo_src = None
	photo_src_big = None
	photo_src_small = None
	saved = None
	post_id = None


SaveWallPhotoResponseModel = array


SaveResponseModel = array


class SearchResponse(BaseResponse):
	count = None
	items = None


class WallUploadResponse(BaseResponse):
	hash = None
	photo = None
	server = None
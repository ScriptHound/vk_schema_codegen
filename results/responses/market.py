


class AddAlbumResponse(BaseResponse):
	response = None


class AddResponse(BaseResponse):
	response = None


class CreateCommentResponse(BaseResponse):
	response = None


class DeleteCommentResponse(BaseResponse):
	response = None


class GetAlbumByIdResponse(BaseResponse):
	response = None


class GetAlbumsResponse(BaseResponse):
	response = None


class GetByIdExtendedResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetCategoriesNewResponse(BaseResponse):
	response = None


class GetCategoriesResponse(BaseResponse):
	response = None


class GetCommentsResponse(BaseResponse):
	response = None


class GetGroupOrdersResponse(BaseResponse):
	response = None


class GetOrderByIdResponse(BaseResponse):
	response = None


class GetOrderItemsResponse(BaseResponse):
	response = None


class GetOrdersExtendedResponse(BaseResponse):
	response = None


class GetOrdersResponse(BaseResponse):
	response = None


class GetExtendedResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class RestoreCommentResponse(BaseResponse):
	response = None


class SearchExtendedResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


class AddAlbumResponse(BaseResponse):
	market_album_id = None


class AddResponse(BaseResponse):
	market_item_id = None


CreateCommentResponseModel = None


DeleteCommentResponseModel = None


class GetAlbumByIdResponse(BaseResponse):
	count = None
	items = None


class GetAlbumsResponse(BaseResponse):
	count = None
	items = None


class GetByIdExtendedResponse(BaseResponse):
	count = None
	items = None


class GetByIdResponse(BaseResponse):
	count = None
	items = None


class GetCategoriesNewResponse(BaseResponse):
	items = None


class GetCategoriesResponse(BaseResponse):
	count = None
	items = None


class GetCommentsResponse(BaseResponse):
	count = None
	items = None


class GetGroupOrdersResponse(BaseResponse):
	count = None
	items = None


class GetOrderByIdResponse(BaseResponse):
	order = None


class GetOrderItemsResponse(BaseResponse):
	count = None
	items = None


class GetOrdersExtendedResponse(BaseResponse):
	count = None
	items = None
	groups = None


class GetOrdersResponse(BaseResponse):
	count = None
	items = None


class GetExtendedResponse(BaseResponse):
	count = None
	items = None


class GetResponse(BaseResponse):
	count = None
	items = None


RestoreCommentResponseModel = None


class SearchExtendedResponse(BaseResponse):
	count = None
	items = None


class SearchResponse(BaseResponse):
	count = None
	items = None
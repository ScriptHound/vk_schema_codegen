


class GetFavoriteStickersResponse(BaseResponse):
	response = None


class GetProductsResponse(BaseResponse):
	response = None


class GetStickersKeywordsResponse(BaseResponse):
	response = None


GetFavoriteStickersResponseModel = array


GetProductsResponseModel = array


class GetStickersKeywordsResponse(BaseResponse):
	count = None
	dictionary = None
	chunks_count = None
	chunks_hash = None
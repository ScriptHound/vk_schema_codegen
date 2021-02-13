


class CreateResponse(BaseResponse):
	response = None


class DeleteResponse(BaseResponse):
	response = None


class EditResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetUploadURLResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class CreateResponse(BaseResponse):
	owner_id = None
	card_id = None


class DeleteResponse(BaseResponse):
	owner_id = None
	card_id = None
	error = None


class EditResponse(BaseResponse):
	owner_id = None
	card_id = None


GetByIdResponseModel = array


GetUploadURLResponseModel = string


class GetResponse(BaseResponse):
	count = None
	items = None
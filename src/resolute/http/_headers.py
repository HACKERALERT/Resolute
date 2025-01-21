class Headers:
	_dict: dict[str, str]

	def __init__(self) -> None:
		self._dict = {}

	def __getitem__(self, key: str) -> str:
		key = key.lower()
		if key not in self._dict:
			raise KeyError
		return self._dict[key]

	def __setitem__(self, key: str, value: str) -> None:
		self._dict[key.lower()] = value

	def __contains__(self, key: str) -> bool:
		return key.lower() in self._dict

	def keys(self) -> list[str]:
		return list(self._dict.keys())

	def values(self) -> list[str]:
		return list(self._dict.values())

	def to_bytes(self) -> bytes:
		return b"\r\n".join(k.encode() + b": " + self._dict[k].encode() for k in self._dict.keys())

def headers_from_bytes(data: bytearray) -> Headers:
	lines = [i.decode(encoding="utf-8", errors="strict") for i in data.split(b"\r\n")]
	headers: Headers = Headers()
	for line in lines:
		if not line:
			continue
		parts = line.split(":", 1)
		key, value = parts[0], parts[1].lstrip(" ")
		headers[key] = value
	return headers

namespace py myservice

// Definição do tipo complexo
struct ComplexType {
  1: string name,
  2: i32 age
}

// Estruturas para requisição e resposta
struct LongRequest {
  1: i64 value
}

struct LongResponse {
  1: i64 value
}

struct EightLongsRequest {
  1: i64 v1,
  2: i64 v2,
  3: i64 v3,
  4: i64 v4,
  5: i64 v5,
  6: i64 v6,
  7: i64 v7,
  8: i64 v8
}

struct StringRequest {
  1: string value
}

struct StringResponse {
  1: string value
}

struct ComplexRequest {
  1: ComplexType complex
}

struct ComplexResponse {
  1: ComplexType complex
}

// Serviço
service TestService {
  void NoArgsNoReturn(),
  LongResponse OneLong(1: LongRequest request),
  LongResponse EightLongs(1: EightLongsRequest request),
  StringResponse OneString(1: StringRequest request),
  ComplexResponse ComplexOperation(1: ComplexRequest request)
}

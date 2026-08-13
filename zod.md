# Validate: zod

Đang có sẵn `@hookform/resolvers` ở chia-keo (dependency) nhưng chưa thấy
schema zod thật nào trong code — resolver đã cắm chỗ, thiếu lib validate.

```
pnpm add zod
```

```ts
import { z } from "zod";

const splitFormSchema = z.object({
  title: z.string().min(1, "Bắt buộc nhập tên"),
  amount: z.number().positive("Số tiền phải > 0"),
  participants: z.array(z.string()).min(2, "Cần ít nhất 2 người"),
});

type SplitForm = z.infer<typeof splitFormSchema>;
```

```tsx
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

const form = useForm<SplitForm>({ resolver: zodResolver(splitFormSchema) });
```

Dùng chung schema cho validate server-side (Hono route handler) — 1 schema,
validate cả client (react-hook-form) và server, tránh lệch rule.

## Lựa chọn khác (không dùng)

- **valibot** — API tương tự zod, bundle nhỏ hơn nhiều (tree-shakeable), đáng
  đổi qua nếu bundle size app trở thành vấn đề. Ecosystem/resolver ít hơn zod.
- **yup** — cũ hơn, API kém gọn hơn zod, ít lý do chọn cho project mới.

## Cách đổi lib sau này

Định nghĩa schema tập trung 1 file/module riêng theo domain (ví dụ
`schemas/split.ts`), form và route handler import từ đó — đổi lib validate
chỉ sửa các file schema, không đụng chỗ dùng.

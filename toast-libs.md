# Thư viện toast/notification

## Đang dùng (chia-keo): sonner

Trước đó chia-keo tự viết toast riêng (`src/components/Toast.tsx` — context +
portal + 3 variant success/error/info). Đã đổi sang **sonner** (2026-08-10):
nhẹ (~3-5KB), animation đẹp sẵn, ít code hơn tự viết, custom style vẫn được
qua CSS variables/`classNames`.

```
pnpm add sonner
```

```tsx
// main.tsx / root layout
import { Toaster } from "sonner";

<Toaster position="bottom-center" />;
```

```ts
import { toast } from "sonner";

toast.success("Đã lưu");
toast.error("Không lưu được");
toast("Thông tin chung"); // info/default
```

### Custom CSS

4 cách, không bị khóa style mặc định:

- Inline: `toast.success("msg", { style: {...} })`
- `classNames` prop trên `<Toaster>` — gán class cho `toast`/`title`/
  `description`/`actionButton`, chỉnh bằng CSS/Tailwind ngoài.
- CSS variables Sonner expose sẵn: `--normal-bg`, `--normal-text`,
  `--success-bg`... override bằng CSS thường.
- `unstyled: true` trên `<Toaster>` — bỏ hết style mặc định, tự vẽ lại từ đầu
  (cách cũ Toast.tsx làm).

## Lựa chọn khác (không dùng)

- **react-hot-toast** — nhẹ tương tự sonner, ổn định lâu, API đơn giản, custom
  style dễ. Đáng cân nhắc nếu sonner có vấn đề tương thích React version.
- **react-toastify** — nặng hơn 2 cái trên, nhiều tính năng hơn (progress bar,
  pause on hover, RTL) nhưng style mặc định cũ, cần chỉnh nhiều mới đẹp.

## Cách đổi lib sau này

Không có điểm chặn riêng như `Avatar.tsx` — sonner gọi trực tiếp qua
`import { toast } from "sonner"` ở từng file cần. Đổi lib phải sửa từng chỗ
gọi `toast(...)`.

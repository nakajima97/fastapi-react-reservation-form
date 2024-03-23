import "./App.css";
import { Box } from "@mui/system";
import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import "dayjs/locale/ja";
import * as dayjs from "dayjs";
import { Controller, useForm } from "react-hook-form";
import { Button, TextField } from "@mui/material";

dayjs.locale("ja");

function App() {
  const { register, control } = useForm();

  return (
    <>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <Box>
          <Controller
            name="date"
            control={control}
            render={({ field }) => <DatePicker {...field} label="予約日時" />}
          />
        </Box>
        <Box>
          <TextField {...register("name")} label="名前" />
        </Box>
        <Box>
          <TextField
            {...register("emailAddress")}
            label="メールアドレス"
            type="email"
          />
        </Box>
        <Box>
          <TextField {...register("phoneNumber")} label="電話番号" />
        </Box>
        <Button type="submit">Submit</Button>
      </LocalizationProvider>
    </>
  );
}

export default App;

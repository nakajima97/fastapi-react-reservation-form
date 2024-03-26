import "./App.css";
import { Box } from "@mui/system";
import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import "dayjs/locale/ja";
import * as dayjs from "dayjs";
import { Controller, useForm } from "react-hook-form";
import { Button, Grid, TextField } from "@mui/material";
import axios from "axios";

dayjs.locale("ja");

axios.defaults.withCredentials = true;

function App() {
  const { register, control, handleSubmit } = useForm();

  const onSubmit = (data: any) => {
    console.log(data);
    const postData = {
      reservation_date: data.date.format("YYYY-MM-DD"),
      name: data.name,
      email_address: data.emailAddress,
      phone_number: data.phoneNumber,
    };
    console.log({ postData });

    const header = {
      "Content-Type": "application/json",
    };

    axios
      .post("http://localhost:8000/reservation", postData, header)
      .then((res) => {
        console.log(res);
      });
  };

  return (
    <>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <form onSubmit={handleSubmit(onSubmit)}>
          <Grid container spacing={2}>
            <Grid item xs={12}>
              <Controller
                name="date"
                control={control}
                render={({ field }) => (
                  <DatePicker
                    {...field}
                    label="予約日時"
                    sx={{ width: "100%" }}
                  />
                )}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField {...register("name")} label="名前" fullWidth />
            </Grid>
            <Grid item xs={12}>
              <TextField
                {...register("emailAddress")}
                label="メールアドレス"
                type="email"
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                {...register("phoneNumber")}
                label="電話番号"
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <Button type="submit" fullWidth>
                予約
              </Button>
            </Grid>
          </Grid>
        </form>
      </LocalizationProvider>
    </>
  );
}

export default App;

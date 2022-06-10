<template>
  <div class='App'>
    <h1>Users and Photos</h1>
    <div> 
    <Bar v-if="loaded" :chartData="chartData" :options="options"></Bar>
    <br>
    </div>
    <Doughnut v-if="loaded" :chartData="DoughnutData" :options="options"></Doughnut>
    <br>
    <Line v-if="loaded" :chartData="LineData" :options="options"></Line>
    <br>
    <!-- <div v-for="user in usernames" :key="user.name" class="user">
    {{ user }}</div> -->
    <br>
    <Radar v-if="loaded" :chartData="RadarData" :options="options"></Radar>
  </div>
</template>

<script>
import axios from 'axios'
import { Bar, Doughnut, Line, Radar} from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement, PointElement, LineElement, RadialLinearScale} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, ArcElement, PointElement, LineElement, RadialLinearScale)

export default {
    name: 'App',
    components:  { Bar, Doughnut, Line, Radar } ,
    data() {
      return {
        usernames : [],
        total_likes: [],
        total_photos: [],
        loaded: false,
        chartData: [],
        DoughnutData: [],
        locations: [],
        users: [],
        LineData: [],
        tim: [],
        created_at: [],
        RadarData: [],
        userss: [],
        tf: [],
        tl: [],
        search: null

      }
    },
    methods: {
      getBarData() {
        this.loaded = false;
        axios.get('http://localhost:5050/select_pie')
        .then(res => {
          console.log(res);
          this.loaded = true;
          for (let i = 0; i < 10; i++) {
            this.usernames.push(res['data'][i]["username"]);
            this.total_likes.push(res['data'][i]["total_likes"]);
            this.total_photos.push(res['data'][i]["total_photos"]);
            
          }
          this.chartData = {
            labels: this.usernames,
            datasets:  [{
              label: "Top Users for likes",
              data: this.total_likes,
              backgroundColor: ["rgba(255,99,132,1)"],
              borderColor: ["rgba(255,99,132,0.2)"],
              borderWidth: 1
            }],
          }
            
          this.options = {
            scales: {
              yAxes: [
                {
                  ticks: {
                    beginAtZero: true
                  }
                }
              ]
            },
            maintainAspectRatio: false,
            title: {
              display: true,
              text: "text"
            }
          }
        })
        .catch(err => {
          console.log(err);
        });
      },
      getDoughnutData() {
        this.loaded = false;
        axios.get('http://localhost:5050/select_locations')
        .then(res => {
          console.log(res);
          this.loaded = true;
          for (let i = 0; i < 10; i++) {
            this.locations.push(res['data'][i]["location"]);
            this.users.push(res['data'][i]["user"]);
            
          }
          console.log(this.users);
          this.DoughnutData = {
            labels: this.locations,
            datasets:  [{
              label: 'По локациям',
              data: this.users,
              backgroundColor: ['#AB274F', '#F19CBB', '#E52B50', '#9F2B68', '#ED3CCA', '#CD2682', '#FF033E', '#9966CC', '#CD9575', '#FFFAFA'],
              
          }]
          }

          this.options = {
            responsive: true,
            maintainAspectRatio: false
          }
        })
        .catch(err => {
          console.log(err);
        });
      },
      getLineData() {
        this.loaded = false;
        axios.get('http://localhost:5050/select_updates')
        .then(res => {
          console.log(res);
          this.loaded = true;
          for (let i = 0; i < 200; i++) {
            this.tim.push(res['data'][i]["tim"]);
            this.created_at.push(res['data'][i]["created_at"]);
            
          }
          console.log(this.users);
          this.LineData = {
            labels: this.created_at,
            datasets:  [{
              label: 'Amount of photo added by date',
              data: this.tim,
              backgroundColor: ['#AB274F'],
              
          }]
          }

          this.options = {
            responsive: true,
            maintainAspectRatio: false
          }
        })
        .catch(err => {
          console.log(err);
        });
      },
      getRadarData() {
        this.loaded = false;
        axios.get('http://localhost:5050/select_radar')
        .then(res => {
          console.log(res);
          this.loaded = true;
          for (let i = 0; i < 20; i++) {
            this.userss.push(res['data'][i]["username"]);
            this.tl.push(res['data'][i]["total_likes"]);
            this.tf.push(res['data'][i]["total_photos"]);
            
          }
          this.RadarData = {
            labels: this.userss,
            datasets:  [
              {
                label: 'Likes',
                backgroundColor: 'rgba(179,181,198,0.2)',
                pointBackgroundColor: 'rgba(179,181,198,1)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgba(179,181,198,1)',
                data: this.tl
              },
              {
                 label: 'Photos',
                 backgroundColor: 'rgba(255,99,132,0.2)',
                 pointBackgroundColor: 'rgba(255,99,132,1)',
                 pointBorderColor: '#fff',
                 pointHoverBackgroundColor: '#fff',
                 pointHoverBorderColor: 'rgba(255,99,132,1)',
                 data: this.tf
              }
            ]
          }

          this.options = {
            responsive: true,
            maintainAspectRatio: false
          }
        })
        .catch(err => {
          console.log(err);
        });
      }
      

    },

    mounted() {
      this.getBarData();
      this.getDoughnutData();
      this.getLineData();
      this.getRadarData();
    }
  
}





</script>

<style>
.App{
  max-width: 800px;
  margin: 0 auto;
}

.photo{
  padding: 20px;
  margin: 20px 0;
  box-sizing: border-box;
  background: #eee;
}
</style>